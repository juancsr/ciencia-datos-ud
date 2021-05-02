import { GET_TERRITORIOS, TERRITORIO_SELECTED } from '../types/territoriosTypes';
import { GET, BASE_URL } from './requestHandler';

export const GetAllTerritorios = () => async (dispatch) => {
  const territoriosResponse = await GET(`${BASE_URL}territorios`);
  try {
    dispatch({
      type: GET_TERRITORIOS,
      payload: territoriosResponse.data,
    });
  } catch (error) {
    console.log(error);
  }
};

export const SelectTerritorio = (territorio) => async (dispatch) => {
  dispatch({
      type: TERRITORIO_SELECTED,
      payload: territorio, 
  });
}