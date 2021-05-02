import React, { useState } from 'react';
import { GetAllLaboratorios } from '../redux/actions/laboratoriosActions';
import { GetAllTerritorios } from '../redux/actions/territoriosActions';
import { connect } from 'react-redux';
import SelectLab from './select-lab';
import SelectTerritorio from './select-territorio';

const XSelect = ({
	GetAllLaboratorios,
	GetAllTerritorios
}) => {
	const options = ['Territorio', 'Laboratorio'];
	const [axisSelected, selectAxis] = useState(null);

	const handleChange = (e) => {
		console.log(e.target.value)
		switch (e.target.value) {
			case 'Territorio':
			default:
				GetAllTerritorios();
				selectAxis(<SelectTerritorio />);
				break;
			case 'Laboratorio':
				GetAllLaboratorios();
				selectAxis(<SelectLab />);
				break;
		}
		// console.log(laboratoriosReducer, territoriosReducer);
	}

	return (
		<>
			<label>Eje X</label>

			<select onChange={handleChange}>
				{/* <option value="a">a</option> */}
				{options.map((option, i) =>  <option value={option} key={i}>{option}</option>)}
			</select>
			
			<div>{axisSelected}</div>
		</>
	)
}

export default connect(null, {GetAllLaboratorios, GetAllTerritorios})(XSelect);
