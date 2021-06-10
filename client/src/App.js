import './App.css';
import Form from './components/Form'
import StaticMap from './components/StaticMap'

function App() {

  const setPosition = (data) => {
    console.log(`X: ${data.x}\nY: ${data.y}`)
  }

  return (

    <div className="App">
      <h1>Restaurant Finder</h1>
      <Form setPosition={setPosition}/>
      <br /> <br /> <br />
      <StaticMap/>
    </div>
  )
}

export default App;
