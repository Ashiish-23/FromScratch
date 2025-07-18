import React from 'react';
import { Image, StyleSheet, View } from 'react-native';
import Carousel from 'react-native-reanimated-carousel';
import { heightPercentageToDP as hp, widthPercentageToDP as wp } from 'react-native-responsive-screen';

const ITEM_WIDTH = wp(100);  // Full screen width
const ITEM_HEIGHT = hp(30);  // Adjust height as needed
const IMAGE_RADIUS = 30; // Pill-shaped rounding

export default function ImageSlider({ data = [] }) {
  return (
    <Carousel
      width={ITEM_WIDTH}
      height={ITEM_HEIGHT}
      data={data}
      loop
      autoPlay
      autoPlayInterval={4000}
      scrollAnimationDuration={1000}
      renderItem={({ item, index }) => (
        <View
          key={item.id}
          style={styles.slide}
          accessible
          accessibilityLabel={`Slider image ${index + 1}`}
        >
          <Image
            source={item.image}
            style={styles.image}
            resizeMode="cover"
          />
        </View>
      )}
      panGestureHandlerProps={{ activeOffsetX: [-10, 10] }}
      mode="parallax"
      modeConfig={{
        parallaxScrollingScale: 0.85,
        parallaxScrollingOffset: 90,
        parallaxAdjacentItemScale: 0.8,
      }}
      pagingEnabled
      snapEnabled
      style={{ alignSelf: 'center' }}
    />
  );
}

const styles = StyleSheet.create({
  slide: {
    width: ITEM_WIDTH,
    height: ITEM_HEIGHT,
    alignItems: 'center',
    justifyContent: 'center',
    overflow: 'hidden',
    backgroundColor: '#f3f4f6',
    marginHorizontal: 4, // Small margin for separation
  },
  image: {
    width: '100%',
    height: '100%',
    borderRadius: IMAGE_RADIUS, // Fully rounded (pill)
  },
});
