//init function

//fill out dropdown with pitching and batting

//fill out dropdown with player names based on selection

//calls pagebuilder function that draws the charts



function lineChartBuilder(player){

    // Use D3 to select the dropdown menu
    var dropdownMenu = d3.select("#selOption");
    // Assign the value of the dropdown menu option to a variable
    var selection = dropdownMenu.property("value");

    d3.json(`/api/${selection}`).then((data) => {
  
      //console.log(player);
  
      // Filter data.samples based on subject
      filteredData = data.data.filter(row => row[1] == player);
  
      // The array that you get back you are interested in [0]
      playerData = filteredData[0]

      console.log(playerData)
  
  
    })
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

      console.log(firstOne);
  
      lineChartBuilder(firstOne);
    
  
    })
  }

  
  function optionChanged(selection) {
  
    lineChartBuilder(selection);
  }
  
  
  init()

  d3.selectAll("#selOption").on("change", init);
  
  