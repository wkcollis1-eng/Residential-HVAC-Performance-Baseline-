# Home Assistant Implementation

This directory contains a complete Home Assistant implementation of the HVAC Performance Baseline monitoring system.

## Quick Start

### Option 1: Single-File Package (Recommended)

1. **Download the package:**

   ```bash
   mkdir -p /config/packages
   curl -o /config/packages/hvac_baseline.yaml \
     https://raw.githubusercontent.com/wkcollis1-eng/Residential-HVAC-Performance-Baseline-/main/homeassistant/packages/hvac_baseline.yaml
   ```

2. **Enable packages in `configuration.yaml`:**

   ```yaml
   homeassistant:
     packages: !include_dir_named packages
   ```

3. **Customize entity IDs:**
   
   Open `hvac_baseline.yaml` and replace the placeholder entities:
   
   | Placeholder | Replace With | Example |
   |-------------|--------------|---------|
   | `climate.THERMOSTAT_1F` | Your 1st floor thermostat | `climate.living_room` |
   | `climate.THERMOSTAT_2F` | Your 2nd floor thermostat | `climate.upstairs` |
   | `sensor.OUTDOOR_TEMP_HIGH_TODAY` | Today's high temperature | `sensor.weather_daily_high` |
   | `sensor.OUTDOOR_TEMP_LOW_TODAY` | Today's low temperature | `sensor.weather_daily_low` |

4. **Restart Home Assistant**

5. **Wait 7 days** for statistical bounds to populate

### Option 2: Manual Integration

If you prefer to integrate specific sensors into your existing configuration, see the "Individual Sensors" section in the main [README](../README.md#option-2-individual-sensors).

## What's Included

### Sensors

| Sensor | Description | Update Frequency |
|--------|-------------|------------------|
| `sensor.hvac_hdd65_today` | Today's heating degree days | Continuous |
| `sensor.hvac_runtime_per_hdd_today` | Today's efficiency (min/HDD) | Continuous |
| `sensor.hvac_runtime_per_hdd_7_day` | 7-day rolling efficiency | Continuous |
| `sensor.hvac_runtime_per_hdd_mean` | Statistical mean | Daily |
| `sensor.hvac_runtime_per_hdd_upper_bound` | Mean + 2σ threshold | Daily |
| `sensor.hvac_zone_balance_ratio` | 2F runtime % of total | Continuous |
| `sensor.hvac_chaining_index` | Multi-zone coordination | Continuous |
| `sensor.hvac_filter_hours_remaining` | Until filter change | Hourly |

### Alerts (Binary Sensors)

| Alert | Triggers When |
|-------|---------------|
| `binary_sensor.hvac_runtime_per_hdd_high_alert` | Efficiency >2σ above mean (4+ days data) |
| `binary_sensor.hvac_zone_imbalance_alert` | Zone balance <35% or >65% |
| `binary_sensor.hvac_filter_change_alert` | Filter runtime ≥1000 hours |

### Automations

| Automation | Schedule | Function |
|------------|----------|----------|
| `hvac_baseline_capture_daily_hdd` | 11:55 PM | Captures HDD, updates rolling window |
| `hvac_baseline_capture_daily_runtime_per_hdd` | 11:56 PM | Captures efficiency for statistics |
| `hvac_baseline_update_filter_runtime` | Hourly | Accumulates filter runtime |
| `hvac_baseline_reset_monthly` | 1st of month | Resets monthly HDD counter |
| `hvac_baseline_reset_yearly` | Jan 1 | Resets yearly HDD counter |

## Customization

### Single-Zone Systems

If you have a single-zone system:

1. Remove all `*_2f_*` entities
2. Simplify `hvac_total_heat_runtime_today` to just reference 1F
3. Remove `hvac_zone_balance_*` sensors
4. Remove `hvac_chaining_index` (requires 2+ zones)

### Different Weather Sources

The package assumes you have daily high/low temperature sensors. Common sources:

**Pirate Weather (HACS):**

```yaml
sensor.OUTDOOR_TEMP_HIGH_TODAY: sensor.pirate_weather_today_high
sensor.OUTDOOR_TEMP_LOW_TODAY: sensor.pirate_weather_today_low
```

**OpenWeatherMap:**

```yaml
sensor.OUTDOOR_TEMP_HIGH_TODAY: sensor.openweathermap_forecast_temperature_high
sensor.OUTDOOR_TEMP_LOW_TODAY: sensor.openweathermap_forecast_temperature_low
```

**NWS (National Weather Service):**

```yaml
# NWS provides forecasts via attributes - you may need template sensors
```

### Adjusting Thresholds

**Filter replacement interval:**
Default is 1000 hours. Adjust in `sensor.hvac_filter_hours_remaining`:

```yaml
{{ (YOUR_HOURS - states('input_number.hvac_filter_runtime_hours') | float(0)) | round(0) }}
```

**Zone balance thresholds:**
Default is 35-65% (±15% from 50%). Adjust in `binary_sensor.hvac_zone_imbalance_alert`.

**Statistical bounds:**
Default is ±2σ. For tighter control, change to 1.5σ in the upper/lower bound sensors.

## Troubleshooting

### "Unknown" Values After Restart

The rolling windows need time to populate. After a fresh install:

- HDD rolling sum: 7 days
- Runtime/HDD statistics: 4+ days for alerts to enable

### Alerts Not Triggering

Check `sensor.hvac_runtime_per_hdd_data_count`. Alerts require ≥4 valid data points to avoid false positives during initialization.

### Incorrect HDD Values

Verify your outdoor temperature sensors are reporting in Fahrenheit. The HDD calculation assumes °F:

```text
HDD = max(65 - mean_temp, 0)
```

### Zone Balance Always 50%

Ensure both thermostat binary sensors are correctly detecting heating state. Check:

```yaml
{{ state_attr('climate.YOUR_THERMOSTAT', 'hvac_action') }}
```

Should return `heating` when actively heating.

## Data Export

The package doesn't include CSV export by default. To add daily logging:

```yaml
shell_command:
  append_hvac_daily: >
    echo "{{ now().strftime('%Y-%m-%d') }},{{ states('sensor.hvac_hdd65_today') }},{{ states('sensor.hvac_runtime_per_hdd_today') }},{{ states('sensor.hvac_chaining_index') }}" >> /config/hvac_daily.csv

automation:
  - id: hvac_export_daily
    alias: "HVAC: Export Daily Data"
    trigger:
      - platform: time
        at: "23:58:00"
    action:
      - service: shell_command.append_hvac_daily
```

## Dashboard

A sample Lovelace dashboard using ApexCharts is available in `dashboards/energy_performance.yaml`. Requires:

- [ApexCharts Card](https://github.com/RomRider/apexcharts-card) (HACS)
- [Mushroom Cards](https://github.com/piitaya/lovelace-mushroom) (HACS, optional)

## Support

- **Issues:** [GitHub Issues](https://github.com/wkcollis1-eng/Residential-HVAC-Performance-Baseline-/issues)
- **Discussions:** [GitHub Discussions](https://github.com/wkcollis1-eng/Residential-HVAC-Performance-Baseline-/discussions)

## License

MIT License - See [LICENSE](../LICENSE)
