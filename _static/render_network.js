function RenderGraph(nodes, links, me) {
    const NODE_R = 12;
    const gData = {
        nodes: nodes, links: links
    }

    const Graph = ForceGraph();
    const elem = document.getElementById('graph');
    const tooltip = document.getElementById('tooltip');
    Graph(elem)
        .graphData(gData)
        .width(500)
        .height(500)
        .linkWidth(5)
        .nodeCanvasObject((node, ctx) => {
            ctx.lineWidth = 5;
            ctx.strokeStyle = 'white';
            ctx.beginPath(); ctx.arc(node.x, node.y, NODE_R, 0, 2 * Math.PI, false); ctx.closePath();
            ctx.stroke();

            // Render node label
            ctx.font = "8px Arial";
            ctx.textAlign = "center";
            ctx.textBaseline = "middle";
            
            // Node color
            if (node.id == me){
                ctx.fillStyle = "coral";
                ctx.fill();
                ctx.fillStyle = "black";
                ctx.fillText(node.id + "/You", node.x, node.y);
            } else {
                ctx.fillStyle = "lightblue";
                ctx.fill();
                ctx.fillStyle = "black";
                ctx.fillText(node.id, node.x, node.y);
            }
        })
        .nodePointerAreaPaint((node, color, ctx) => {
            ctx.fillStyle = color;
            ctx.beginPath();
            ctx.arc(node.x, node.y, NODE_R, 0, 2 * Math.PI, false);
            ctx.fill();
        })
        .linkColor((link) => link.show ? 'white' : 'black')
        .onNodeHover(node => {
            if (node) {
                tooltip.style.display = 'block';
                tooltip.innerHTML = `👤 Player: ${node.id} <br> ℹ️ Threshold: ${node.example_threshold}`;
            }
            else {
                tooltip.style.display = 'none';
                tooltip.innerHTML = '';
            }
        });
      
    // Move tooltip with mouse
    elem.addEventListener('mousemove', e => {
        tooltip.style.left = (e.pageX + 20) + 'px';
        tooltip.style.top = (e.pageY + 20) + 'px';
    });

    Graph.d3Force('link').distance(100);
    Graph.d3Force('center', null);
}