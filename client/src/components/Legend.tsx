import styles from "./Legend.module.css";

const POSITION_CLASSES: Record<string, string> = {
  bottomleft: 'leaflet-bottom leaflet-left',
  bottomright: 'leaflet-bottom leaflet-right',
  topleft: 'leaflet-top leaflet-left',
  topright: 'leaflet-top leaflet-right',
}

interface LegendProps {
  position?: 'bottomleft' | 'bottomright' | 'topleft' | 'topright';
}

function Legend({ position = 'bottomright' }: LegendProps) {
  const positionClass = POSITION_CLASSES[position] || POSITION_CLASSES.bottomright;
  return (
    <div className={`leaflet-control ${positionClass}`}>
      <div className={styles.legend}>
        <h4>Legend</h4>
        <ul>
          <li className={styles.item}>
            <div className={styles.dot} style={{ backgroundColor: '#0d9488' }} />
            <span className={styles.label}>No Tsunami</span>
          </li>
          <li className={styles.item}>
            <div className={styles.dot} style={{ backgroundColor: '#f97316' }} />
            <span className={styles.label}>Tsunami</span>
          </li>
        </ul>
      </div>
    </div>
  );
}

export default Legend;