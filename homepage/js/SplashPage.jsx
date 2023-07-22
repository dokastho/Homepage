import React from 'react'
import Lottie from 'react-lottie-player';
import animationData from '../lotties/launcher-arrow.json';

class SplashPage extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      doPlay: false
    }

    this.playAnimation = this.playAnimation.bind(this);
  }

  playAnimation() {
    this.setState({ doPlay: true });
  }

  render() {
    const { doPlay } = this.state;

    return (
      <div className='mobile'>
        <h1>Hey There 👋</h1>
        <h5>Thanks for visiting.</h5>
        <br />
        <br />
        <div className='launcher-button' onClick={this.playAnimation}>
          <h5>Explore My Portfolio</h5>
          {/* {
            doPlay ? (
              <Lottie
                className='launcher-button-animation'
                play
                loop={false}
                animationData={animationData}
              />
            ) : (
              <Lottie
                className='launcher-button-animation'
                goTo={0}
                animationData={animationData}
              />
            )
          } */}
        </div>
      </div>
    );
  }
}

export default SplashPage;
