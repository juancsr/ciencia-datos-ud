import React, {useState} from 'react';
import { GetGraph } from '../../redux/actions/graphActions';
import { connect } from 'react-redux';

const Graph = ({ columnsReducer, graphReducers, GetGraph }) => {
    //const [url, setUrl] = useState('');
    const [limit, setLimit] = useState(10);

    const handleClick = () => {
        console.log("clicked")

        const x = columnsReducer.selectedColumns;
        const y = 'cantidad';
        const order = 'asc';
        GetGraph(x,y,limit,order);
    };

    return (
        <div>
            <div>
                <label for="limite">Limite</label>
                <input name="limite" type="number" onChange={e => setLimit(e.target.value)}/>
            </div>
            <button type="submit" onClick={handleClick}>Mostrar gráfico</button>
            <div>
                Graph!
                <div dangerouslySetInnerHTML={{ __html: graphReducers.graph}} />
            </div>
        </div>
    );
}

const mapStateToProps = ({columnsReducer, graphReducers}) => ({columnsReducer, graphReducers});

export default connect(mapStateToProps, {GetGraph})(Graph);