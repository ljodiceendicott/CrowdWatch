function reset(start) {
  var table = document.getElementById("values");
  const dropdown = document.getElementById("loc");
  fetch("/currentvalues")
    .then((response) => response.json())
    .then((data) => {
      for (var i = start; i < data.account.locations.length; i++) {
        var loc = data.account.locations[i];
        const location = {
          name: loc.name,
          maxCap: loc.maxCap,
          count: loc.count,
          idx: i,
        };
        locations.push(location);
        // console.log(location.name.slice(0, location.name.length / 2));
        var shortName = location.name.slice(0, location.name.length / 2);
        //Use a Drop down menu that will show the location names
        //It will then populate the textarea with the location number

        //Need to figure out how to add variable amount to dropdown menu
        let option = document.createElement("option");
        option.setAttribute("value", location.idx);

        let optionText = document.createTextNode(location.name);
        option.appendChild(optionText);

        dropdown.appendChild(option);
        // console.log(data.account.locations[i]);
      }
    });
  return locations[0];
}
function changeval() {
  var selection = document.getElementById("loc");
  console.log(selection.value);
  console.log(locations[selection.value]);
}
