import React, { useState } from 'react';
import { GetGraph } from '../../redux/actions/graphActions';
import { connect } from 'react-redux';
import DataTable from './data-table';

const Graph = ({
    columnsReducer, 
    graphReducers, 
    territoriosReducer, 
    GetGraph,
    laboratoriosReducer,
}) => {
    //const [url, setUrl] = useState('');
    const [limit, setLimit] = useState(10);
    const [asc, setAsc] = useState(true);
	  const info = [{
        laboratorio_vacuna: "PFIZER",
        nom_territorio: "BOGOTA D.C.",
        cantidad: 757475,
    },
    {
        laboratorio_vacuna: "PFIZER",
        nom_territorio: "AMAZONAS",
        cantidad: 1,
    },
    {
        laboratorio_vacuna: "PFIZER",
        nom_territorio: "ANTIOQUIA",
        cantidad: 70000,
    }];

    const handleClick = () => {
        console.log("clicked")

        const x = columnsReducer.selectedColumns;
        const y = ['cantidad'];
        const order = asc ? 'asc' : 'desc';
        const lastElement = columnsReducer.selectedColumns.slice(-1)[0];
        let filter = '';
        switch (lastElement) {
            case "nom_territorio":
                filter = territoriosReducer.territorio !== "TODOS" ? [territoriosReducer.territorio] : '';
                break;
            case "laboratorio_vacuna":
                filter = laboratoriosReducer.laboratorio !== "TODOS" ? [laboratoriosReducer.laboratorio] : '';
                break;
        }
        //GetGraph(x, y, limit, order, filter);
    };

    return (
        <div>
            <div>
                <br></br>
                <label for="limite"><b>Limite:</b> </label>
                <input name="limite" value={limit} type="number" onChange={e => setLimit(e.target.value)} />
            </div>
            <div>
                <br></br>
                <label for="asc"><b>Ascendente:</b> </label>
                <input name="asc" type="checkbox" value={asc} checked={asc} onChange={() => setAsc(!asc)}></input>
            </div>
            <div style={{ margin: 'auto', textAlign: 'center' }}>
                <button type="submit" onClick={handleClick}>Mostrar gráfico</button>
            </div>
            <div>
	    	{/*<div dangerouslySetInnerHTML={{ __html: graphReducers.graph }} />*/}
                <DataTable data={info}/>
            </div>
        </div>
    );
}

const mapStateToProps = ({ columnsReducer, graphReducers, territoriosReducer, laboratoriosReducer }) => (
    { columnsReducer, graphReducers, territoriosReducer, laboratoriosReducer }
);

export default connect(mapStateToProps, { GetGraph })(Graph);
