import { GET_GRAPH } from '../types/graphTypes';
import { GET, BASE_URL } from './requestHandler';

export const GetGraph = () => async (dispatch) => {
    const graphResponse = await GET(`${BASE_URL}graph`);
    try {
        dispatch({
            type: GET_GRAPH,
            payload: graphResponse.data,
        });
    } catch (error) {
        console.log(error);
    }
};