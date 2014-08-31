// ******************************************************************
// ************************* Simple function ************************
// ******************************************************************

function d3BubbleChartSample(bubbleContainer, diameter, staticURL, bubblePadding, bubbleNodeDy, bubbleNodeTextAnchor) {
    var format = d3.format(",d"),
        color = d3.scale.category20c();

    var bubble = d3.layout.pack()
        .sort(null)
        .size([diameter, diameter])
        .padding(bubblePadding);

    var svg = d3.select(bubbleContainer).append("svg")
        .attr("width", diameter)
        .attr("height", diameter)
        .attr("class", "bubble");

    d3.json(staticURL + "js/d3_bubble_chart_flare.json", function(error, root) {
      var node = svg.selectAll(".node")
          .data(bubble.nodes(classes(root))
          .filter(function(d) { return !d.children; }))
        .enter().append("g")
          .attr("class", "node")
          .attr("transform", function(d) {
              return "translate(" + d.x + "," + d.y + ")";
          });

      node.append("title")
          .text(function(d) {
              return d.className + ": " + format(d.value);
          });

      node.append("circle")
          .attr("r", function(d) { return d.r; })
          .style("fill", function(d) { return color(d.packageName); });

      node.append("text")
          .attr("dy", bubbleNodeDy)
          .style("text-anchor", bubbleNodeTextAnchor)
          .text(function(d) { return d.className.substring(0, d.r / 3); });
    });

    // Returns a flattened hierarchy containing all leaf nodes under the root.
    function classes(root) {
      var classes = [];

      function recurse(name, node) {
        if (node.children) node.children.forEach(function(child) { recurse(node.name, child); });
        else classes.push({packageName: name, className: node.name, value: node.size});
      }

      recurse(null, root);
      return {children: classes};
    }

    d3.select(self.frameElement).style("height", diameter + "px");
}
