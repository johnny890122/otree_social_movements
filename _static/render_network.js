function RenderGraph(nodes, links, me) {
    const elem = document.getElementById('graph');
    const tooltip = document.getElementById('tooltip');

    const rect = elem.getBoundingClientRect();
    let width = rect.width;
    let height = rect.height;
    let NODE_R = Math.max(5, Math.min(width, height) / 30);
    const Graph = ForceGraph();

    nodes.forEach(node => {
        node.x = node.x * width*3;
        node.y = node.y * height*3;
    });

    const gData = { nodes: nodes, links: links };

    Graph(elem)
        .graphData(gData)
        .width(width)
        .height(height)
        .linkWidth(5)
        .nodeCanvasObject((node, ctx) => {
            ctx.lineWidth = 5;
            ctx.strokeStyle = 'white';
            ctx.beginPath(); 
            ctx.arc(node.x, node.y, NODE_R, 0, 2 * Math.PI, false); ctx.closePath();
            ctx.stroke();

            ctx.font = "7px Arial";
            ctx.textAlign = "center";
            ctx.textBaseline = "middle";
            
            // Node color
            if (node.id == me){
                ctx.fillStyle = "coral";
                ctx.fill();
                ctx.fillStyle = "black";
                ctx.fillText(node.id + "(You)", node.x, node.y);
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
        })
      
    // Move tooltip with mouse
    elem.addEventListener('mousemove', e => {
        tooltip.style.left = (e.pageX + 20) + 'px';
        tooltip.style.top = (e.pageY + 20) + 'px';
    });
}