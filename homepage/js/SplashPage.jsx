import PropTypes from 'prop-types';
import React from 'react'
import Lottie from 'react-lottie-player';
import animationData from '../lotties/launcher-arrow.json';

class SplashPage extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      doPlay: false,
      fadeIn: false,
    }

    this.playAnimation = this.playAnimation.bind(this);
  }

  componentDidMount() {
    setTimeout(() => {
      this.setState({ fadeIn: true });
    }, 300)
  }

  playAnimation() {
    this.setState({ doPlay: true });
    const { loadSite } = this.props;
    setTimeout(() => {
      this.setState({ fadeIn: false });
    }, 400)
    setTimeout(() => {
      loadSite();
    }, 600)
  }

  render() {
    const { doPlay, fadeIn } = this.state;

    return (
      <div className={`mobile fade-${fadeIn ? 'in' : 'out'}`}>
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
