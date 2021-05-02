import { GET_GRAPH } from '../types/graphTypes';

const INITIAL_STATE = {
    graph: null,
};

const reducer = (state = INITIAL_STATE, action) => {
    switch (action.type) {
        case GET_GRAPH:
            return {...state, graph: action.payload};
        default:
            return state;
    }
}

export default reducer;