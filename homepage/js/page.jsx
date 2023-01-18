import PropTypes from 'prop-types';
import { react } from 'react'

class Page extends react.Component {

  constructor(props) {
    super(props);
    this.state = {
      // state attributes go here
      pageId: 0,
      title: "",
      description: "",
      body: "",
      route: "",
    };
  }

  componentDidMount() {
    this.setState(this.props);
  }

  render() {
    const { } = this.state;
    return (
      <div>
      </div>
    );
  }
}

Page.propTypes = {
  // prop types go here
  pageId: PropTypes.number.isRequired,
  title: PropTypes.string.isRequired,
  description: PropTypes.string.isRequired,
  body: PropTypes.string.isRequired,
  route: PropTypes.string.isRequired
};

Page.defaultProps = {
  // default prop values go here if not required
};

export default Page
