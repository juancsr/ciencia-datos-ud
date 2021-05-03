import React, { useState, useEffect } from 'react';
import { connect } from 'react-redux';
import { AddSelectedColumn } from '../redux/actions/columnActions';

const SelectedColumns = ({ columnsReducer, AddSelectedColumn }) => {

    const [selectedColumns, setSelectedColumn] = useState(columnsReducer.selectedColumns);

    const handleClick = (index) => () => {
        console.log(index)
        const aux = selectedColumns;
        aux.splice(index, 1);
        console.log(aux);
        setSelectedColumn(aux);
        console.log(selectedColumns)
        AddSelectedColumn(selectedColumns);
    };

    return (
        <div>
            {selectedColumns.map((column, i) =>
                <div style={{margin: '1px black solid'}} key={i}>
                    {columnsReducer.columnList[column]}
                    <button onClick={handleClick(i)}>X</button>
                </div>)
            }
        </div>
    )
};

const mapStateToProps = ({ columnsReducer }) => ({ columnsReducer });
//const mapDispatchToProps = ({ AddSelectedColumn }) => { AddSelectedColumn };

export default connect(mapStateToProps, {AddSelectedColumn})(SelectedColumns);
