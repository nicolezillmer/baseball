//init function

//fill out dropdown with pitching and batting

//fill out dropdown with player names based on selection

//calls pagebuilder function that draws the charts



function lineChartBuilder(player){

    // Use D3 to select the dropdown menu
    var dropdownMenu = d3.select("#selOption");
    // Assign the value of the dropdown menu option to a variable
    var selection = dropdownMenu.property("value");

    if (selection == 'batters'){
      d3.json(`/api/${selection}`).then((data) => {
  
      //console.log(player);
  
      // Filter data.data based on player
      filteredData = data.data.filter(row => row[1] == player);
  
      // The array that you get back you are interested in [0]
      playerData = filteredData[0]

      console.log(playerData)

      x = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
      y = playerData.slice(2,24)

      var trace1 = {
        x : x,
        y : y,
        type : "line"
      };

      var data1 = [trace1]

      var layout1 = {
        title : "Batting Average"
      };

      Plotly.newPlot("graph1", data1, layout1);
      Plotly.purge("graph2");
  
  
    })

    } else if (selection == "pitchers"){

      //GET ERA DATA
      d3.json("/api/era").then((data) => {

          // Filter data.data based on player
        filteredData = data.data.filter(row => row[1] == player);
        // The array that you get back you are interested in [0]
        playerData = filteredData[0]
        console.log(playerData)

        x = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
        era = playerData.slice(2,21)
        
        var eraTrace = {
          x : x,
          y : era,
          type : "line"
        };

        var eraData = [eraTrace]
          
        var eraLayout = {
          title : "Era Data"
        };

        Plotly.newPlot("graph1", eraData, eraLayout);
      });
      
      
      d3.json("/api/whip").then((data) => {

          // Filter data.data based on player
          filteredWHIPData = data.data.filter(row => row[1] == player);
          // The array that you get back you are interested in [0]
          playerWHIPData = filteredWHIPData[0]
          
          //console.log(playerERAData)

          x = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019];
          whip = playerWHIPData.slice(2,21);

          var whipTrace = {
            x : x,
            y : whip,
            type : "line"
          };
  
          var whipData = [whipTrace]
            
          var whipLayout = {
            title : "WHIP Data"
          };
  
          Plotly.newPlot("graph2", whipData, whipLayout);


      });




      

    };

    
  }
  
  
  function init() {

      // Use D3 to select the dropdown menu
    var dropdownMenu = d3.select("#selOption");
    // Assign the value of the dropdown menu option to a variable
    var selection = dropdownMenu.property("value");

    //console.log(selection);
    
    // Fill dropdown with IDs
    // Get firstOne id and call buildPage with that id
    
    d3.json(`/api/${selection}`).then((data) => {

      //console.log(data)

    
      var selector = d3.select("#selPlayer");

      selector.html("");
    
      data.data.forEach((row) => {
        selector
          .append("option")
          .text(row[1])
          .property("value", row[1])
      })
    
  
      firstOne = data.data[0][1];
  
      lineChartBuilder(firstOne);
    
  
    })
  }

  
  function optionChanged(selection) {
  
    lineChartBuilder(selection);
  }
  
  
  init()

  d3.selectAll("#selOption").on("change", init);
  
  