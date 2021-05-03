import React, {useState} from 'react';
import { GetGraph } from '../../redux/actions/graphActions';
import { connect } from 'react-redux';

const Graph = ({ columnsReducer, graphReducers, GetGraph }) => {
    //const [url, setUrl] = useState('');
    const [limit, setLimit] = useState(10);
    const [asc, setAsc] = useState(true);

    const handleClick = () => {
        console.log("clicked")

        const x = columnsReducer.selectedColumns;
        const y = ['cantidad'];
        const order = asc ? 'asc' : 'desc';
        GetGraph(x,y,limit,order);
    };

    return (
        <div>
            <div>
                <br></br>
                <label for="limite"><b>Limite:</b> </label>
                <input name="limite" value={limit} type="number" onChange={e => setLimit(e.target.value)}/>
            </div>
            <div>
                <br></br>
                <label for="asc"><b>Ascendente:</b> </label>
                <input name="asc" type="checkbox" value={asc} checked={asc} onChange={() => setAsc(!asc)}></input>
            </div>
            <div style={{margin: 'auto', textAlign: 'center'}}>
                <button type="submit" onClick={handleClick}>Mostrar gráfico</button>
            </div>
            <div>
                <div dangerouslySetInnerHTML={{ __html: graphReducers.graph}} />
            </div>
        </div>
    );
}

const mapStateToProps = ({columnsReducer, graphReducers}) => ({columnsReducer, graphReducers});

export default connect(mapStateToProps, {GetGraph})(Graph);