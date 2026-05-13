import styles from './App.module.css'
import Header from './components/Header'
import EarthquakeMap from './pages/EarthquakeMap'
import Overview from './pages/Overview'

function App() {
  return (
    <div className={styles.main}>
      <Header />
      <div className={styles.content}>
        <Overview />
        <EarthquakeMap />
      </div>
    </div>
  )
}

export default App