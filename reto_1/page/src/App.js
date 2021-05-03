import './App.css';
import XAsisSelect from './components/xaxis-select';
import Graph from './components/graph/graph';

function App() {
  return (
    <div>
      <h1 style={{textAlign: 'center', margin: 'auto', fontSize: 20}}>Vacunas Covid-19 2021</h1>
      <div>
        <div id="menu-options">
          <XAsisSelect />
        </div>
        <div id="graph">
          <Graph />
        </div>
      </div>
    </div>
  );
}

export default App;
