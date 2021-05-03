import { GET_ALL_COLUMNS, SELECT_COLUMN, ADD_COLUMN } from '../types/columnsTypes';

const INITIAL_STATE = {
    columnList: [],
    selectedColumn: 'a_o',
    selectedColumns: [],
};

const reducer = (state = INITIAL_STATE, action) => {
    switch (action.type) {
        case GET_ALL_COLUMNS:
            return {...state, columnList: action.payload};
        case SELECT_COLUMN:
            return {...state, selectedColumn: action.payload};
        case ADD_COLUMN:
            return {...state, selectedColumns: action.payload};
        default:
            return state;
    }
}

export default reducer;