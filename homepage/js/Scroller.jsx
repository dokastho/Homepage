import PropTypes from 'prop-types';
import React from 'react';
import Lottie from 'react-lottie-player';
import animationData from '../lotties/arrow-down.json';

const lottieLen = 28;

class Scroller extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      lastFired: 0,
      scrollSum: 0,
      coolDown: 500,
      thresh: 2000,
    };
    this.undoScroll = this.undoScroll.bind(this);
  }

  componentDidMount() {
    window.addEventListener("wheel", this.handleScroll);
    this.setState({ lastFired: Date.now() });
  }

  componentWillUnmount() {
    window.removeEventListener("wheel", this.handleScroll);
  }

  handleScroll = (event) => {
    // ignore event if it's happening too soon
    const timestamp = Date.now();
    const { lastFired, coolDown } = this.state;
    if (timestamp - lastFired < coolDown) {
      return;
    }
    const { scrollSum, thresh } = this.state;
    const { onScroll, isTop, isBottom } = this.props;
    const currentScrollPosition = event.wheelDeltaY;

    // ignore event if moving past boundaries
    const isUp = currentScrollPosition > 0;
    if (isUp && isTop) {
      return;
    } else if (!isUp && isBottom) {
      return;
    }

    const updatedScrollSum = scrollSum + currentScrollPosition;
    const delta = Math.abs(updatedScrollSum)

    if (delta > thresh) {
      if (0 < updatedScrollSum) {
        onScroll("up");
      } else if (updatedScrollSum < 0) {
        onScroll("down");
      }
      this.setState({
        lastFired: timestamp,
        scrollSum: 0,
      });
    } else {
      this.setState({
        scrollSum: updatedScrollSum,
      })
      this.undoScroll(currentScrollPosition);
    }
  }

  undoScroll(ss) {
    // undo after 1s
    setTimeout(() => {
      this.setState((prevState) => ({ scrollSum: prevState.scrollSum - ss }))
    }, 1000)
  }

  render() {
    const { scrollSum, thresh } = this.state;
    const frac = Math.abs(lottieLen * scrollSum / thresh);
    const isUp = scrollSum < 0;

    return (
      <div className='scroller-svg-div'>
        {scrollSum === 0 ? null : (
          <Lottie
            className='scroller-svg'
            goTo={frac}
            animationData={animationData}
            style={{ transform: `rotate(${isUp ? 0 : 180}deg)` }}
          />
        )}
      </div>
    );
  }
}



Scroller.propTypes = {
  // prop types go here
  // onScroll
  isTop: PropTypes.bool.isRequired,
  isBottom: PropTypes.bool.isRequired,
};

export default Scroller
