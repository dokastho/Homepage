import PropTypes from 'prop-types';
import React from 'react'

class Scroller extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      scrollSum: 0,
      thresh: 1000,
    };
  }

  componentDidMount() {
    window.addEventListener("wheel", this.handleScroll);
  }

  componentWillUnmount() {
    window.removeEventListener("wheel", this.handleScroll);
  }

  handleScroll = (event) => {
    const { scrollSum, thresh } = this.state;
    const { onScroll, pageNum } = this.props;
    const currentScrollPosition = event.wheelDeltaY;

    const updatedScrollSum = scrollSum + currentScrollPosition;
    const delta = Math.abs(updatedScrollSum)

    if (delta > thresh) {
      if (0 < updatedScrollSum) {
        const newPageNum = pageNum - 1;
        if (onScroll(newPageNum)) {
          this.setState({
            scrollSum: 0,
          });
        }
      } else if (updatedScrollSum < 0) {
        const newPageNum = pageNum + 1;
        if (onScroll(newPageNum)) {
          this.setState({
            scrollSum: 0,
          });
        }
      }

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
      <div></div>
    );
  }
}



Scroller.propTypes = {
  // prop types go here
  // onScroll
  pageNum: PropTypes.number.isRequired
};

export default Scroller
