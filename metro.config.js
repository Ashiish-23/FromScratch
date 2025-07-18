const { getDefaultConfig } = require("expo/metro-config");
const { withNativeWind } = require('nativewind/metro');
// metro.config.js
const { wrapWithReanimatedMetroConfig } = require('react-native-reanimated/metro-config');

 
const config = getDefaultConfig(__dirname)
 
module.exports = withNativeWind(config, { input: './global.css' })
module.exports = wrapWithReanimatedMetroConfig(config);