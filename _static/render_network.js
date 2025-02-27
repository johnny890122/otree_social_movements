function renderGraph(nodes, links, me) {
    const NODE_R = 12;
    const gData = {
        nodes: nodes, links: links
    }

    const Graph = ForceGraph();
    const elem = document.getElementById('graph');
    Graph(elem)
        .graphData(gData)
        .width(1200)
        .height(500)
        .linkWidth(5)
        .linkColor(["black"])
        .nodeCanvasObject((node, ctx) => {
            ctx.lineWidth = 2.5;
            ctx.strokeStyle = '#568EA6';
            ctx.beginPath(); ctx.arc(node.x, node.y, NODE_R, 0, 2 * Math.PI, false); ctx.closePath();
            ctx.stroke();

            // Render node label
            ctx.font = "8px Arial";
            ctx.textAlign = "center";
            ctx.textBaseline = "middle";
            
            // Node color
            if (node.id == me){
                ctx.fillStyle = "red";
                ctx.fill();
                ctx.fillStyle = "black";
                ctx.fillText(node.id + "/You", node.x, node.y);
            }
            else{
                ctx.fillStyle = "white";
                ctx.fill();
                ctx.fillStyle = "black";
                ctx.fillText(node.id, node.x, node.y);
            }
        })
        .linkColor((link) => link.show ? 'black' : 'white')

    Graph.d3Force('link').distance(100);
    Graph.d3Force('center', null);
}