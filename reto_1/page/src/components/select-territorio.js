import React from 'react';
import { SelectTerritorio } from '../redux/actions/territoriosActions';
import { connect } from 'react-redux';

const CompSelectTerritorio = ({
    SelectTerritorio,
    territoriosReducer
}) => {
    console.log(territoriosReducer);
    const handleChange = (e) => {
        console.log(e.target.value);
        SelectTerritorio(e.target.value);
    }
    return (
        <div>
            <br></br>
            <label><b>LISTA DE TERRITORIOS: </b></label>
            <br></br>
            <select onChange={handleChange}>
                <option disabled>Selecciona uno</option>
                <option value={"TODOS"} default>TODOS</option>
                {Object.keys(territoriosReducer.listaTerritorios).map((key) => {
                    const value = territoriosReducer.listaTerritorios[key];
                    return <option value={value} key={key}>{value}</option>;
                })}
            </select>
        </div>

    )
}

const mapStateToProps = ({ territoriosReducer }) => ({ territoriosReducer });

export default connect(mapStateToProps, { SelectTerritorio })(CompSelectTerritorio);