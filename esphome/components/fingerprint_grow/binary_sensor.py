import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import binary_sensor
from esphome.const import CONF_ICON, ICON_KEY_PLUS
from . import CONF_FINGERPRINT_GROW_ID, FingerprintGrowComponent

DEPENDENCIES = ["fingerprint_grow"]

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(CONF_FINGERPRINT_GROW_ID): cv.use_id(FingerprintGrowComponent),
        cv.Optional("fingerprint_enrolling"): binary_sensor.binary_sensor_schema(
            icon=ICON_KEY_PLUS,
        ),
        cv.Optional("sensing_pin"): binary_sensor.binary_sensor_schema(
            icon="mdi:fingerprint",
        ),
    }
)


async def to_code(config):
    hub = await cg.get_variable(config[CONF_FINGERPRINT_GROW_ID])

    for key in [
        CONF_FINGERPRINT_COUNT,
        CONF_STATUS,
        CONF_CAPACITY,
        CONF_SECURITY_LEVEL,
        CONF_LAST_FINGER_ID,
        CONF_LAST_CONFIDENCE,
    ]:
        if key not in config:
            continue
        conf = config[key]
        sens = await binary_sensor.new_binary_sensor(conf)
        cg.add(getattr(hub, f"set_{key}_binary_sensor")(sens))
