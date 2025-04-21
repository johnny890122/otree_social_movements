function RenderGraph(nodes, links, me, is_practice) {
    const elem = document.getElementById('graph');
    elem.style.border = is_practice ? "2px solid white" : "2px solid black";
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

    const nodeStrokeColor = is_practice ? 'white' : 'black';
    const linkShowColor = is_practice ? 'white' : 'black';
    const linkHideColor = is_practice ? 'black' : 'white';

    Graph(elem)
        .graphData(gData)
        .width(width)
        .height(height)
        .linkWidth(5)
        .nodeCanvasObject((node, ctx) => {
            ctx.lineWidth = 3;
            ctx.strokeStyle = nodeStrokeColor;
            ctx.beginPath(); 
            ctx.arc(node.x, node.y, NODE_R, 0, 2 * Math.PI, false); ctx.closePath();
            ctx.stroke();

            ctx.font = "6px Arial";
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
        .linkColor((link) => link.show ? linkShowColor : linkHideColor)
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