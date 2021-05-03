import { GET_TERRITORIOS, TERRITORIO_SELECTED, TERRITORIOS } from '../types/territoriosTypes';

const INITIAL_STATE = {
    listaTerritorios: [],
    territorio: null,
    territorios: [],
};

const reducer = (state = INITIAL_STATE, action) => {
    switch (action.type) {
        case GET_TERRITORIOS:
            return {...state, listaTerritorios: action.payload};
        case TERRITORIO_SELECTED:
            return {...state, territorio: action.payload};
        case TERRITORIOS:
            return {...state, territorios: action.payload};
        default:
            return state;
    }
}

export default reducer;