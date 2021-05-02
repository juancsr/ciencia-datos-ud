import { GET_LABORATORIOS, LABORATORIO_SELECTED } from '../types/laboratoriosTypes';

const INITIAL_STATE = {
    listaLaboratorios: [],
    laboratorio: null,
};

const reducer = (state = INITIAL_STATE, action) => {
    switch (action.type) {
        case GET_LABORATORIOS:
            return {...state, listaLaboratorios: action.payload};
        case LABORATORIO_SELECTED:
            return {...state, laboratorio: action.payload};
        default:
            return state;
    }
}

export default reducer;