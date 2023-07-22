import PropTypes from 'prop-types';
import React from 'react'
import Lottie from 'react-lottie-player';
import animationData from '../lotties/launcher-arrow.json';

class SplashPage extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      doPlay: false,
    }

    this.playAnimation = this.playAnimation.bind(this);
  }

  playAnimation() {
    const { loadSite } = this.props;
    this.setState({ doPlay: true });
    loadSite();
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
          {
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
          }
        </div>
      </div>
    );
  }
}

SplashPage.propTypes = {
  // prop types go here
  // loadSite
}


export default SplashPage;
