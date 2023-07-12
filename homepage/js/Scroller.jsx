import PropTypes from 'prop-types';
import React from 'react'

class Scroller extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      lastFired: 0,
      scrollSum: 0,
      coolDown: 250,
      thresh: 1000,
    };
  }

  componentDidMount() {
    window.addEventListener("wheel", this.handleScroll);
    this.setState({ lastFired: Date.now() });
  }

  componentWillUnmount() {
    window.removeEventListener("wheel", this.handleScroll);
  }

  handleScroll = (event) => {
    const timestamp = Date.now();
    const { lastFired, coolDown } = this.state;
    if (timestamp - lastFired < coolDown) {
      return;
    }
    const { scrollSum, thresh } = this.state;
    const { onScroll } = this.props;
    const currentScrollPosition = event.wheelDeltaY;

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
    }
  }

  render() {
    const { scrollSum, thresh } = this.state;
    const frac = 100 * scrollSum / thresh;
    return (
      <div>{`${frac}%`}</div>
    );
  }
}



Scroller.propTypes = {
  // prop types go here
  // onScroll
  pageNum: PropTypes.number.isRequired
};

export default Scroller
