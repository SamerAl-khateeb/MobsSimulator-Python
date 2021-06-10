// File: dcfm_simulator.js
// Author: Samer Al-khateeb
//
// This file contains several function for simulating DCFM events and display the result in a table.
////////////////////////////////////////////////////////////////////////////////////////////////////

////////////////// Code for Running the DCFM Simulation Many Times////////////////////////// 

function simulationResultsSummmary(resultsArray, numOfSims)
  {
    var succcess_counter = 0;
    var fail_counter = 0;
    var succcess_counter_Percent = 0;

    for (var i = 0; i < resultsArray.length; ++i )
    {
        if (resultsArray[i] == "Success")
          {
            succcess_counter = succcess_counter + 1;
          }
        else
          {
            fail_counter = fail_counter + 1;
          }
    }

    succcess_counter_Percent = (succcess_counter/numOfSims) * 100;

    output1.innerHTML = succcess_counter_Percent.toFixed(1) + " % of the times DCFM succeeded!";
  }

function runSim()
  {
    
    var numofinvprac = parseInt(document.getElementById('invnumofprac').value);  //the number of invited people
    var T_o = parseFloat(document.getElementById('threshold').value) / 100; // the threshold of DCFM success
    var numofruns = parseInt(document.getElementById('numofsim').value); // number of simulation
    var numofpowact = parseInt(document.getElementById('numofpow').value); // number of powerful actors
		
    var ACounter = new Array( numofruns );  //declearing ACounter array and initialize all its elements to zero
    for ( var i = 0; i < numofruns; ++i )
          {
            ACounter[ i ] = 0 ;
            ACounter[ i ] += numofpowact;   //addinng the number of powerful actors to the Acting Practitioners Counter

          }

    var WCounter = new Array( numofruns );   //declearing WCounter array and initialize all its elements to zero
    for ( var i = 0; i < numofruns; ++i )
        { 
          WCounter[ i ] = 0 ;
        }


    var PECounter = new Array( numofruns );  //declearing PECounter array and initialize all its elements to zero
    for ( var i = 0; i < numofruns; ++i )
        {
          PECounter[ i ] = 0 ;
        }


    var AACounter = new Array( numofruns );  //declearing AACounter array and initialize all its elements to zero
    for ( var i = 0; i < numofruns; ++i )
        {
          AACounter[ i ] = 0 ;
        }


    var participation_rate = new Array( numofruns );  //declearing participation_rate array and initialize all its elements to zero
    for ( var i = 0; i < numofruns; ++i )
        {
          participation_rate[ i ] = 0;
        }


    var result = new Array( numofruns );  //declearing result array and initialize all its elements to empty string
    for ( var i = 0; i < numofruns; ++i )
        {
          result[ i ] = '' ;
        }

	
	  if (numofpowact > numofinvprac) //check if we have more powerful actors than the number of invited people, the script will not run
		  {	
			   resetAll();
			   window.alert("the number of Powerful Actors can not be more than the number of Invited People. Please adjust the numbers");
		  }
	
	  else //if the number of powerful actors equal or same as number of invited people then the script will run
	    {

  	    for ( var i = 0; i < numofruns; ++i)     // the variable i is used for the number of runs/simulations
  		   {

            for ( var j = 0; j < numofinvprac; ++j)     // the variable j is used for the number of individuals inserted
            {
                var p_interest = parseInt(RandomOneOf(["0", "1"]));

                var p_control = parseInt(RandomOneOf(["0", "1"]));

                //have interest and have control, practitioner will act       
                if ((p_interest === 1) && (p_control === 1))
                    {
                      p_decision = 'Act';
                      ACounter[i] = ACounter[i] + 1;
                      }

                //have interest but no control, practitioner will act or withdraw 
                if ((p_interest === 1) && (p_control === 0))
                    {
                      p_decision = RandomOneOf(['Act','Withdraw']);

                      if (p_decision === 'Act')
                          {
                            ACounter[i] = ACounter[i] + 1;
                          }

                      else
                          {
                            WCounter[i] = WCounter[i] + 1;
                          }
                    }

                //No interest but have control, practitioner will act or withdraw 
                if ((p_interest === 0) && (p_control === 1))
                    {
                      p_decision = RandomOneOf(['Withdraw','PowerExchange']);

                      if (p_decision === 'Withdraw')
                        {
                          WCounter[i] = WCounter[i] + 1;
                        }

                      else
                        {
                          PECounter[i] = PECounter[i] + 1;
                        }
                    }
      
                //No interest and No control, practitioner will withdraw or Act Against 
                if ((p_interest === 0) && (p_control === 0))
                  {
                    p_decision = RandomOneOf(['Withdraw','ActAgainst']);

                    if (p_decision === 'Withdraw')
                      {
                        WCounter[i] = WCounter[i] + 1;
                      }
                    else
                      {
                        AACounter[i] = AACounter[i] + 1;
                      }
                  }

            	
              participation_rate[i] = parseFloat(ACounter[i] / numofinvprac);
              
              
            	if ( participation_rate[i] > T_o) 
                	{ 
                  		result[i] = "Success"; 
                	}
            	else 
                	{ 
                  		result[i] = "Fail"; 
                	}

            }


            simulationResultsSummmary(result, numofruns);

            outputTable("Simulation Result:", numofinvprac, ACounter, WCounter, PECounter, AACounter, result, document.getElementById('output2'));

  		}
  	}
  }



	////////////////////////// function to print the simulation result as a Table ///////////////////
  	function outputTable(heading, numofinvprac, ACounter, WCounter, PECounter, AACounter, result, output2)
    	{

     		var content = "<h2>" + heading + "</h2> <table border ='1'><thead><th> Simulation Number</th><th> Number of Invited Practitioners </th><th> Number of Acting </th><th> Number of Withdraw </th><th> Number of Power Exchange</th><th> Number of Acting Against</th><th> DCFM Result </th></thead><tbody>";

      	var Alength = result.length; // get array's length once before loop
   
        for ( var i = 0; i < Alength; ++i )   
              {
                content += "<tr><td>" + i + "</td><td>" + numofinvprac + "</td><td>" + ACounter[ i ] + "</td><td>" + WCounter[ i ]+ "</td><td>" + PECounter[ i ]+ "</td><td>" + AACounter[ i ]+ "</td><td>" + result[ i ]+ "</td></tr>" ;
              } // end for

        content += "</tbody></table>";
        output2.innerHTML = content; // place the table in the output element        
    	} // end function outputTable



	////////////////// Function for resetting all input fields and the output table //////////////////////////
  	function resetAll()
  		{
    		document.getElementById('invnumofprac').value = 10;
    		document.getElementById('threshold').value = 50;
    		document.getElementById('numofsim').value = 1;
    		document.getElementById('numofpow').value = 0;
        document.getElementById('output1').innerHTML = "";
    		document.getElementById('output2').innerHTML = "";
  		}




      