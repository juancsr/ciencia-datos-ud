import { GET_LABORATORIOS, LABORATORIO_SELECTED} from '../types/laboratoriosTypes';
import { GET, BASE_URL } from './requestHandler';

export const GetAllLaboratorios = () => async (dispatch) => {
    const laboratoriosResponse = await GET(`${BASE_URL}labs`);
    try {
        dispatch({
            type: GET_LABORATORIOS,
            payload: laboratoriosResponse.data,
        });
    } catch (error) {
        console.log(error);
    }
};

export const SelectLaboratorio = (laboratorio) => async (dispatch) => {
    dispatch({
        type: LABORATORIO_SELECTED,
        payload: laboratorio, 
    });
}