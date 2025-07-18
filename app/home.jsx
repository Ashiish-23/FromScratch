import React from 'react';
import { View, Text, StatusBar, StyleSheet, Image } from 'react-native';
import { SafeAreaView } from 'react-native-safe-area-context';
import { widthPercentageToDP as wp, heightPercentageToDP as hp } from 'react-native-responsive-screen';
import Ionicons from 'react-native-vector-icons/Ionicons';
import { sliderData } from '../constants/index';
import   ImageSlider  from '../components/ImageSlider.jsx'; // Correctly modularized

export default function Home() {
  return (
    <SafeAreaView style={styles.container} edges={["top"]}>
      <StatusBar barStyle="dark-content" />

      {/* Header */}
      <View style={styles.headerRow}>
        <View>
          <Text style={styles.punchlineText}>READY TO</Text>
          <Text style={[styles.punchlineText, { color: '#f43f5e' }]}>WORKOUT</Text>
        </View>
        <View style={styles.avatarContainer}>
          <Image
            style={styles.avatarImage}
            source={require('../assets/images/welcome.png')}
          />
          <View style={styles.notificationBadge}>
            <Ionicons name="notifications" size={hp(2)} color="gray" />
          </View>
        </View>
      </View>

      {/* Image Slider */}
      <View style={{ marginTop: hp(4) }}>
        <ImageSlider data={sliderData} />
      </View>
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
  headerRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    marginHorizontal: wp(5),
    marginTop: hp(2),
  },
  punchlineText: {
    fontSize: hp(3.5),
    fontWeight: 'bold',
    color: '#18181b',
  },
  avatarContainer: {
    alignItems: 'center',
    justifyContent: 'center',
  },
  avatarImage: {
    width: hp(10),
    height: hp(10),
    borderRadius: hp(3.5),
    borderWidth: 3,
    borderColor: '#f43f5e',
  },
  notificationBadge: {
    position: 'absolute',
    bottom: -hp(1),
    right: -wp(1),
    backgroundColor: 'white',
    height: hp(4),
    width: hp(4),
    borderRadius: hp(2),
    alignItems: 'center',
    justifyContent: 'center',
    borderWidth: 2,
    borderColor: '#d4d4d8',
    elevation: 2,
    shadowOpacity: 0.1,
    shadowRadius: 2,
  },
});
