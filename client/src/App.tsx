import styles from './App.module.css'
import Header from './components/Header'
import Overview from './pages/Overview'

function App() {
  return (
    <div className={styles.main}>
      <Header />
      <div className={styles.content}>
        <Overview />
      </div>
    </div>
  )
}

export default App