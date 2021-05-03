import { GET_ALL_COLUMNS, SELECT_COLUMN, ADD_COLUMN } from '../types/columnsTypes';
import { GET, BASE_URL } from './requestHandler';

export const GetAllColumns = () => async (dispatch) => {
    const columnResponse = await GET(`${BASE_URL}columns`);
    try {
        dispatch({
            type: GET_ALL_COLUMNS,
            payload: columnResponse.data,
        });
    } catch (error) {
        console.log(error);
    }
};

export const AddSelectedColumn = (column) => async (dispatch) => {
    dispatch({
        type: ADD_COLUMN,
        payload: column,
    });
}

export const SelectColumn = (column) => async (dispatch) => {
    console.log(column);
    dispatch({
        type: SELECT_COLUMN,
        payload: column,
    });
};