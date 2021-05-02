import { GET_TERRITORIOS, TERRITORIO_SELECTED } from '../types/territoriosTypes';

const INITIAL_STATE = {
    listaTerritorios: [],
    territorio: null,
};

const reducer = (state = INITIAL_STATE, action) => {
    switch (action.type) {
        case GET_TERRITORIOS:
            return {...state, listaTerritorios: action.payload};
        case TERRITORIO_SELECTED:
            return {...state, territorio: action.payload};
        default:
            return state;
    }
}

export default reducer;