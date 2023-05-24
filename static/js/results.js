let data = document.getElementById('data_from_analys')
data = JSON.parse(data.innerHTML)

let plotsContainer = document.getElementById('plots_xy_container')
let plotsParam1Container = document.getElementById('plots_param1_container')
let plotsParam2Container = document.getElementById('plots_param2_container')
let plotsQJcontainer = document.getElementById('plots_QJ_container')

let plotXYholder = document.getElementById('plot_xy_holder')
let plotParam2Holder = document.getElementById('plot_param2_holder')

for (let i = 0; i < data.Q_j_list.length; i++) {
    plot = document.createElement('div');

    Plotly.newPlot(plot, [{
        x: Object.keys(data.Q_j_list[i]),
        y: Object.values(data.Q_j_list[i]),
        mode: 'lines+markers',
        marker: {
            color: 'rgb(255, 0, 0)',
            size: 3
        },
        line: {
            color: 'rgb(55, 128, 191)',
        }
    }], {
        margin: { t: 0 }
    }, { responsive: true });

    plotsQJcontainer.appendChild(plot)
}

{
    if (Object.keys(data.result_2_param).length == 0) {
        plotParam2Holder.remove()
    }
    else {
        plot = document.createElement('div');

        Plotly.newPlot(plot, [{
            x: Object.keys(data.result_2_param),
            y: Object.values(data.result_2_param),
            type: "bar",
        }], {
            margin: { t: 0 }
        }, { responsive: true });

        plotsParam2Container.appendChild(plot)
    }
}



{
    plot = document.createElement('div');

    Plotly.newPlot(plot, [{
        x: Object.keys(data.result_1_param),
        y: Object.values(data.result_1_param),
        type: "bar",
    }], {
        margin: { t: 0 }
    }, { responsive: true });

    plotsParam1Container.appendChild(plot)
}
if (data.xy_list.length == 0) {
    plotXYholder.remove()
}
else {
    for (let i = 0; i < data.xy_list.length; i++) {
        plot = document.createElement('div');
        Plotly.newPlot(plot, [{
            x: data.xy_list[i][0],
            y: data.xy_list[i][1],
            mode: 'lines+markers',
            marker: {
                color: 'rgb(255, 0, 0)',
            },
            line: {
                color: 'rgb(55, 128, 191)',
            }
        }], {
            margin: { t: 0 }
        }, { responsive: true });


        plotsContainer.appendChild(plot)
    }
}


