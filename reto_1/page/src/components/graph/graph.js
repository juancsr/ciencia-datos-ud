import React from 'react';

const Graph = () => {
    const handleClick = () => {
        console.log("clicked")
    };

    return (
        <div>
            <button onClick={handleClick}>Mostrar gráfico</button>
            <div>
                Graph!
            </div>
        </div>
    );
}

export default Graph;