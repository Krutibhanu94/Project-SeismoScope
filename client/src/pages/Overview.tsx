import { useEffect, useState } from "react";
import { getStatistics } from "../services/api";
import StatsCard from "../components/StatsCard";
import styles from "./Overview.module.css";


interface Statistics {
    totalEarthquakes: number;
    averageMagnitude: number;
    tsunamiCount: number;
    tsunamiRate: number;
  }
function Overview() {
  const [stats, setStats] = useState<Statistics | null>(null);

  useEffect(() => { 
    getStatistics().then((data) => setStats(data));
  }, []);
  
  if(!stats) {
    return <p>Loading...</p>;
  } 
  
  return (
    <section id="overview" className={styles.section}>
      <h2 className={styles.title}>Statistics</h2>
      <div className={styles.grid}>
        <StatsCard title="Total Earthquakes" value={stats.totalEarthquakes} />
        <StatsCard title="Average Magnitude" value={stats.averageMagnitude} />
        <StatsCard title="Tsunami Count" value={stats.tsunamiCount} />
        <StatsCard title="Tsunami Rate" value={stats.tsunamiRate} />
      </div>
      
    </section>
  )
}

export default Overview