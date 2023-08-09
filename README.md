# <B>Ripple Energy API integration for Home Assistant<B>

[![hacs_badge](https://img.shields.io/badge/HACS-Default-41BDF5.svg)](https://github.com/hacs/integration)

Use me [Octopus.Energy 🐙](https://share.octopus.energy/iron-moose-196) referral code. You get £50 credit for joining and I get £50 credit.

# Work in progress
- HACS Integration
- Home Assistant UI WorkFlow
- json to Type: Sensors via HACS/HA UI integration

Updated: 9th August, 2023

# Pre Installation
You will require your Ripple Energy members API key as per available here: [Ripple Energy API Key](https://community.rippleenergy.com/new-feature-requests-yyqtfatb/post/ripple-api-yH0cTzuQ4GJMaYV?highlight=l8VWP51eyif7JlZ)

# Installation
<B>HACS<B>
1. Add the https://github.com/MJP-76/RippleEnergyAPI as a "Custom Repository" in HACS (Home Assistant Community Store)
2. Install the integration in HACS
3. Restart Home Assistant

<B>Manual<B>
1. Download the https://github.com/MJP-76/RippleEnergyAPI
2. Copy the folder custom_components/Name: ripple_energy_api from the zip to your config directory
3. Restart Home Assistant

# Post Installation
After restart of Home Assistant, integration can be configured through the integration setup UI

# Generated Type: Sensors
The following Type: Sensors are generated from the Ripple Energy (https://rippleenergy.com/ ) API into Home Assistant

<B>Sensors created<B>


<B>Sensors not created yet<B>

<B>Name:<B> ripple_asset0_generation_this_week_from
<B>Entity:<B> sensor.ripple_asset0_generation_this_week_from
<B>Type:<B> Sensor
—
Name: ripple_asset0_generation_this_week_generated
Entity: sensor.ripple_asset0_generation_this_week_generated
Type: Sensor
—
Name: ripple_asset0_generation_this_week_to
Entity: sensor.ripple_asset0_generation_this_week_to
Type: Sensor
—
Name: ripple_asset0_generation_this_year_earned
Entity: sensor.ripple_asset0_generation_this_year_earned
Type: Sensor
—
Name: ripple_asset0_generation_this_year_from
Entity: sensor.ripple_asset0_generation_this_year_from
Type: Sensor
—
Name: ripple_asset0_generation_this_year_generated
Entity: sensor.ripple_asset0_generation_this_year_generated
Type: Sensor
—
Name: ripple_asset0_generation_this_year_to
Entity: sensor.ripple_asset0_generation_this_year_to
Type: Sensor
—
Name: ripple_asset0_generation_today_earned
Entity: sensor.ripple_asset0_generation_today_earned
Type: Sensor
—
Name: ripple_asset0_generation_today_estimate
binary_Entity: sensor.ripple_asset0_generation_today_estimate
Type: Binary Type: Sensor
—
Name: ripple_asset0_generation_today_from
Entity: sensor.ripple_asset0_generation_today_from
Type: Sensor
—
Name: ripple_asset0_generation_today_generated
Entity: sensor.ripple_asset0_generation_today_generated
Type: Sensor
—
Name: ripple_asset0_generation_today_to
Entity: Entity: sensor.ripple_asset0_generation_today_to
Type: Sensor
—
Name: ripple_asset0_generation_total_earned
Entity: sensor.ripple_asset0_generation_total_earned
Type: Sensor
—
Name: ripple_asset0_generation_total_estimate
binary_Entity: sensor.ripple_asset0_generation_total_estimate
Type: Binary Type: Sensor
—
Name: ripple_asset0_generation_total_from
Entity: sensor.ripple_asset0_generation_total_from
Type: Sensor
—
Name: ripple_asset0_generation_total_generated
Entity: sensor.ripple_asset0_generation_total_generated
Type: Sensor
—
Name: ripple_asset0_generation_total_to
Entity: sensor.ripple_asset0_generation_total_to
Type: Sensor
—
Name: ripple_asset0_generation_yesterday_earned
Entity: sensor.ripple_asset0_generation_yesterday_earned
Type: Sensor
—
Name: ripple_asset0_generation_yesterday_estimate
binary_Entity: sensor.ripple_asset0_generation_yesterday_estimate
Binary Type: Sensor
—
Name: ripple_asset0_generation_yesterday_from
Entity: sensor.ripple_asset0_generation_yesterday_from
Type: Sensor
—
Name: ripple_asset0_generation_yesterday_generated
Entity: sensor.ripple_asset0_generation_yesterday_generated
Type: Sensor
—
Name: ripple_asset0_generation_yesterday_to
Entity: sensor.ripple_asset0_generation_yesterday_to
Type: Sensor
—
Name: ripple_asset0_member_capacity
Entity: sensor.ripple_asset0_member_capacity
Type: Sensor
—
Name: ripple_asset0_member_capacity_units
Entity: sensor.ripple_asset0_member_capacity_units
Type: Sensor
—
Name: ripple_asset0_member_expected_annual_generation
Entity: sensor.ripple_asset0_member_expected_annual_generation
Type: Sensor
—
Name: ripple_asset0_member_expected_annual_generation_units
Entity: sensor.ripple_asset0_member_expected_annual_generation_units
Type: Sensor
—
Name: ripple_asset0_name
Entity: sensor.ripple_asset0_name
Type: Sensor
—
Name: ripple_asset0_status
Entity: sensor.ripple_asset0_status
Type: Sensor
—
Name: ripple_asset0_total_capacity
Entity: sensor.ripple_asset0_total_capacity
Type: Sensor
—
Name: ripple_asset0_total_capacity_units
Entity: sensor.ripple_asset0_total_capacity_units
Type: Sensor
—
Name: ripple_asset0_type
Entity: sensor.ripple_asset0_type
Type: Sensor
—
Name: ripple_email
Entity: sensor.ripple_email
Type: Sensor