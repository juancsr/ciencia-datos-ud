import React, { useState, useEffect } from 'react';
import { GetAllLaboratorios } from '../redux/actions/laboratoriosActions';
import { GetAllTerritorios } from '../redux/actions/territoriosActions';
import { GetAllColumns, SelectColumn, AddSelectedColumn } from '../redux/actions/columnActions';
import { connect } from 'react-redux';
import SelectLab from './select-lab';
import SelectTerritorio from './select-territorio';
import SelectedColumns from './selected-columns';

const XSelect = ({
	columnsReducer,
	GetAllLaboratorios,
	GetAllTerritorios,
	GetAllColumns,
	SelectColumn,
	AddSelectedColumn,
}) => {
	const [axisSelected, selectAxis] = useState(null);

	useEffect(() => {
		GetAllColumns();
	}, []);

	const handleChange = (e) => {
		SelectColumn(e.target.value);
		console.log(e.target.value);
		// switch (e.target.value) {
		// 	case 'nom_territorio':
		// 		GetAllTerritorios();
		// 		selectAxis(<SelectTerritorio />);
		// 		break;
		// 	case 'laboratorio_vacuna':
		// 		GetAllLaboratorios();
		// 		selectAxis(<SelectLab />);
		// 		break;
		// 	default:
		// 		selectAxis(null);
		// 		break;
		// }

		const { selectedColumns } = columnsReducer;

		if (selectedColumns.indexOf(e.target.value) === -1) {
			selectedColumns.push(e.target.value);
		} else {
			selectedColumns.splice(selectedColumns.indexOf(e.target.value), 1);
		}
		
		AddSelectedColumn(selectedColumns);
	}

	useEffect(() => {
		if (columnsReducer.selectedColumns.length === 1) {
			const lastElement = columnsReducer.selectedColumns.slice(-1)[0];
			switch (lastElement) {
				case "nom_territorio":
					GetAllTerritorios();
					selectAxis(<SelectTerritorio />);
					break;
				case "laboratorio_vacuna":
					GetAllLaboratorios();
					selectAxis(<SelectLab />);
					break;
				default:
					selectAxis(null);
					break;
			}
		} else {
			selectAxis(null);
		}
	}, [columnsReducer])
	return (
		<>
			<label><b>Columnas</b></label>

			<select onChange={handleChange}>
				{/* <option value="a">a</option> */}
				{Object.keys(columnsReducer.columnList).map((key) => {
					const value = columnsReducer.columnList[key];
					return <option value={key} key={key}>{value}</option>;
				})}
				{/* {options.map((option, i) =>  <option value={option} key={i}>{option}</option>)} */}
			</select>

			<div>
				<SelectedColumns />
			</div>

			{/* <div>{columnsReducer.selectedColumns.length === 1 ?
					axisSelected :
					<></>
			}</div> */}
			{axisSelected}
		</>
	)
}

const mapStateToProps = ({ columnsReducer }) => ({ columnsReducer })

export default connect(mapStateToProps, { GetAllLaboratorios, GetAllTerritorios, GetAllColumns, SelectColumn, AddSelectedColumn })(XSelect);
