import { react } from 'react'

class T extends react.Component {

  constructor(props) {
    super(props);
    this.state = {
      // state attributes go here
    };
  }

  componentDidMount() {
    const {} = this.props;

    this.setState({});
  }

  render() {
    const { } = this.state;
    return (
      <div>
      </div>
    );
  }
}

T.propTypes = {
  // prop types go here
};

T.defaultProps = {
  // default prop values go here
};

export default T
