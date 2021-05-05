import React, {useState, useEffect} from 'react';

const DataTable = ({data}) => {
    const [headers, setHeaders] = useState([]);
    const [body, setBody] = useState([]);
    
    const extractElements = (jsonObject) => {
        let values = [];
        Object.keys(jsonObject).forEach(key => values.push(jsonObject[key]));
        return values;
    };

    useEffect(() => {
        const keys = Object.keys(data[0]);
        setHeaders(keys);
        const _body = []
        data.forEach(element => _body.push(extractElements(element)));
        setBody(_body);
        console.log(headers, body)
    }, [data]);

    return (
        <table className="">
            {headers.length > 0 ?
                <tr>
                    {headers.map(header => (<th>{header}</th>))}
                </tr>
            : <></>}

            {body.length > 0 ?
                body.map(element => <tr>{ element.map(item => (<td>{item}</td>)) }</tr>)
            : <></>}
        </table>
    );
};

export default DataTable;
