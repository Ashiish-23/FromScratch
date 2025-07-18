import { View, Text, Image, StatusBar, TouchableOpacity, Animated } from 'react-native';
import { widthPercentageToDP as wp, heightPercentageToDP as hp } from 'react-native-responsive-screen';
import { LinearGradient } from 'expo-linear-gradient';
import{ FadeInDown } from 'react-native-reanimated';
import { useRouter } from 'expo-router';

export default function Index() {
  const router = useRouter();
  return (
    <View style={{ flex: 1 }}>
      <StatusBar style="light" />
      
      <Image
        source={require('../assets/images/chest.png')}
        style={{
          position: 'absolute',
          width: '100%',
          height: '100%',
          resizeMode: 'cover', 
        }}
      />

      <LinearGradient
        colors={['transparent', '#18181b']}
        style={{
          flex: 1,
          justifyContent: 'flex-end',
          paddingBottom: 48,
          paddingHorizontal: 24,
        }}
      >
        <Animated.View entering={FadeInDown.delay(100).springify()} style={{ alignItems: 'center' }}>
          <Text style={{ color: '#fff', fontSize: hp(5), fontWeight: 'bold' }}>
            Best <Text style={{ color: '#f43f5e', fontSize: hp(5), fontWeight: 'bold' }}>Workouts</Text>
            </Text>
            <Text style={{ color: '#fff', fontSize: hp(5), fontWeight: 'bold' }}>For you </Text>
        </Animated.View>

        <Animated.View entering={FadeInDown.delay(200).springify()} style={{ alignItems: 'center', marginTop: 16 }}>
            <TouchableOpacity 
              onPress={() => router.push('/home')}
              style={{  alignItems: 'center', height: hp(5), width: wp(50), 
              backgroundColor: '#f43f5e', borderRadius: 25, justifyContent: 'center', 
              borderColor: '#000000', borderWidth: 4 }}>
                <Text style={{ color: '#fff', fontWeight: 'bold', fontSize: hp(3)}}>Get Started</Text>
            </TouchableOpacity>
         </Animated.View>   

      </LinearGradient>
    </View>
  );
}
