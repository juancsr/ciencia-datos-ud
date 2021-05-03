import { combineReducers } from 'redux';
import territoriosReducer from './territoriosReducer';
import laboratoriosReducer from './laboratoriosReducer';
import graphReducers from './graphReducers';
import columnsReducer from './columnsReducers';

export default combineReducers({
    territoriosReducer,
    laboratoriosReducer,
    graphReducers,
    columnsReducer,
});