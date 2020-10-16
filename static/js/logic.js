//init function

//fill out dropdown with pitching and batting

//fill out dropdown with player names based on selection

//calls pagebuilder function that draws the charts



///pagebuilder function
//takes two parameters, the pitcher/batter choice and the player name
//draws charts

// Need an event listener for the dropdown
// optionChanged function
// - That takes as a parameter the user selection

// Plan

// init function 
// 1) Fill out dropdown with all of the ids
// 2) Calls a buildPage function that draws the chart and the panel for the first one

// buildPage function 
// 1) That takes one parameter, which is the subject ID
// 2) Draws our plotly charts and fills the panel

// Need an event listener for the dropdown
// optionChanged function
// - That takes as a parameter the user selection

function pageBuilder(subject){

    d3.json("samples.json").then((data) => {
  
      console.log(subject);
  
      // Filter data.samples based on subject
      filteredData = data.samples.filter(sample => sample.id == subject);
  
      // The array that you get back you are interested in [0]
      subjectData = filteredData[0]
  
  
    })
  }
  
  
  function init() {

      // Use D3 to select the dropdown menu
    var dropdownMenu = d3.select("#selOption");
    // Assign the value of the dropdown menu option to a variable
    var selection = dropdownMenu.property("value");

    console.log(selection);
    
    // Fill dropdown with IDs
    // Get firstOne id and call buildPage with that id
    
    
    d3.json(`/api/${selection}`).then((data) => {

      console.log(data)

    /*
      var selector = d3.select("#selPlayer");
    
      data.names.forEach((ids) => {
        selector
          .append("option")
          .text(ids)
          .property("value", ids)
      })
      */
  
      //firstOne = data.names[0];
  
      //pageBuilder(firstOne);
    
  
    })
  }

  
  function optionChanged(selection) {
  
    pageBuilder(selection);
  }
  
  
  init()

  d3.selectAll("#selOption").on("change", init);
  
  