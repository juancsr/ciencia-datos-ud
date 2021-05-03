import React from 'react';
import { SelectLaboratorio } from '../redux/actions/laboratoriosActions';
import { connect } from 'react-redux';

const CompSelectLab = ({
    SelectLaboratorio,
    laboratoriosReducer
}) => {
    console.log(laboratoriosReducer);
    const handleChange = (e) => {
        console.log(e.target.value);
        SelectLaboratorio(e.target.value);
    }
    return (
        <select onChange={handleChange}>
            <option disabled>Selecciona uno</option>
            <option value={"TODOS"} default>TODOS</option>
            {Object.keys(laboratoriosReducer.listaLaboratorios).map((key) => {
                const value = laboratoriosReducer.listaLaboratorios[key];
                return <option value={value} key={key}>{value}</option>;
            })}
        </select>
    )
}

const mapStateToProps = ({ laboratoriosReducer }) => ({ laboratoriosReducer });

export default connect(mapStateToProps, { SelectLaboratorio })(CompSelectLab);