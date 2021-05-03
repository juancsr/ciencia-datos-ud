import { GET_GRAPH } from '../types/graphTypes';
import { GET, BASE_URL } from './requestHandler';

export const GetGraph = (x, ys, limit, order, filter) => async (dispatch) => {
    const query = `x=${x}&y=${ys}&limit=${limit}&order=${order}&filter=${filter}`
    const graphResponse = await GET(`${BASE_URL}graph?${query}`);
    try {
        dispatch({
            type: GET_GRAPH,
            payload: graphResponse.data,
        });
    } catch (error) {
        console.log(error);
    }
};